# decideAction(for:completionHandler:)

**Framework**: MailKit  
**Kind**: method  
**Required**: Yes

Determines the action that the system takes when it downloads a message.

**Availability**:
- macOS 12.0+

## Declaration

```swift
func decideAction(for message: MEMessage) async -> MEMessageActionDecision?
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func decideAction(for message: MEMessage) async -> MEMessageActionDecision?
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
func decideAction(for message: MEMessage) async -> MEMessageActionDecision?
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

As MailKit downloads messages, it invokes this method to determine what action, if any, it should perform on the message. MailKit initially calls this method before downloading the message content. If you can determine the action to take without requiring the entire body, create a [`MEMessageActionDecision`](memessageactiondecision.md) with an [`MEMessageAction`](memessageaction.md) that indicates the action to take. Use the properties of `message` to determine the action to take. For example, if the user chooses to set the color of messages from a particular person, use the message’s [`fromAddress`](memessage/fromaddress.md) property.

If you can’t determine the action without the entire message content and `bodyData` is `nil`, call the completion handler and pass [`invokeAgainWithBody`](memessageactiondecision/invokeagainwithbody.md) as the decision. MailKit invokes this method again later after the `bodyData` in the message is available.

The following code shows an implementation that sets the color of all messages with Project Mars in the subject to red. Because this example only relies on the [`subject`](memessage/subject.md) of the message, it calls the completion handler with an action immediately.

```swift
func decideActionForMessage(for message: MEMessage, completionHandler: @escaping (MEMessageActionDecision?) -> Void) {
    var action: MEMessageActionDecision? = nil

    // Check if the subject of the email is about Project Mars.
    if message.subject.contains("Project Mars") {
        // Create an action to set the color of the
        // message in the message list to red.
         action = MEMessageActionDecision.action(.setColorActionWith(.red))
    }
    
    // Call the completion handler with the action, if any.
    completionHandler(action)

}
```

> ❗ **Important**:  Always call the completion handler. If you don’t have an action to specify, pass `nil`.

 Always call the completion handler. If you don’t have an action to specify, pass `nil`.

The next example shows a different implementation that relies on the message body content to determine if a message is junk. In this case, when `bodyData` is `nil`, the handler calls the completion handler and passes [`invokeAgainWithBody`](memessageactiondecision/invokeagainwithbody.md).

When MailKit downloads the message content, it invokes this method again. This time, the handler converts the body data to a string. If the string indicates that the message is junk, the handler calls the completion handler passing an action that moves the message to the user’s Junk mailbox.

```swift
func decideActionForMessage(for message: MEMessage, completionHandler: @escaping (MEMessageActionDecision?) -> Void) {
    var action: MEMessageActionDecision? = nil

    // Check if the message content is available.
    if message.bodyData == nil {
        // If it isn't, request a repeat call when it is.
        action = MEMessageActionDecision.invokeAgainWithBody
    } else if let bodyData = message.bodyData,
              let body = String(data: bodyData, encoding: .utf8){
        
        // Determine if the message is junk or not.
        let isJunk = body.contains("Make money fast!")
        
        // If it is, then call the completion handler with an action
        // to move the message to the Junk mailbox.
        if isJunk {
            action = MEMessageActionDecision.action(.moveToJunk)
        }
    }
    
    // Call the completion handler with the action, if any.
    completionHandler(action)

}
```

## Parameters

- `message`: The message the system downloads.
- `completionHandler`: A block you call that indicates the action to perform on the message, or if MailKit should invoke this method again after it downloads the message content.

## See Also

- [class MEMessageAction](memessageaction.md)
  An action the system performs on a message, such as setting a color or archiving it.
- [class MEMessageActionDecision](memessageactiondecision.md)
  The action that the system performs on a message, or a request to ask the action handler again later when the message content is available.
- [MEMessageAction.MessageColor](memessageaction/messagecolor.md)
  A color that the system uses to display a message in the message list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/memessageactionhandler/decideaction(for:completionhandler:))*