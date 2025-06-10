# Creating a communication experience

**Framework**: PermissionKit

Request permission from a parent or guardian to modify a child’s communication rules.

#### Overview

You can enable children to seek permission from a parent or guardian before sending a message to a friend on your app. Communication experiences between children and a parent or guardian using the `PermissionKit` framework are only available through iMessage.

##### Manage Permission Responses

Check a person’s age using [`DeclaredAgeRange`](https://developer.apple.comhttps://developer.apple.com/documentation/declaredagerange/) or your own account systems, then obtain an `AsyncSequence` to manage communication permission responses promptly after someone launches your app. Use [`updates`](communicationlimits/updates.md) to enable your app to run in the background and receive responses. The following code snippet describes how you can set up your app to listen for communication responses.

```swift
let responses = CommunicationLimits.current.permissionResponses
for await response in responses {
    print("Received a communication permission response: \(response)")
}
```

Use `CommunicationLimits/knownhandles(in:)-59j52` to determine the people a parent or guardian approved for their child. Some examples of known handles include a person’s name, or a custom username in your app. This method establishes a connection between your app’s list of trusted entities and the settings a parent or guardian configured for their child in [`CommunicationLimits`](communicationlimits.md). You can conceal UI elements within lists, such as a message preview in a conversation list.

```swift
let knownHandles = CommunicationLimits.current.knownHandles(in: 
[.init(value: "dragonslayer42", 
kind: .custom), .init(value: "progamer67", kind: .custom)])
```

##### Create a Permission Question

To enable the request and response exchange, your app listens for responses to questions with the [`CommunicationTopic`](communicationtopic.md) topic type. When a child performs a communication-oriented action in your app that’s gated by parental permission, create a permission question that the child sends to their parent.

```swift
let question = PermissionQuestion<CommunicationTopic>
(handle: .init(value: "dragonslayer42", kind: .custom))
```

##### Set Permission Choices

Each [`PermissionQuestion`](permissionquestion.md) has a set of possible answer choices, and each answer choice corresponds to a globally unique identifier.

```swift
let approveOneHour = PermissionChoice
(id: AnswerIdentifier.approveOneHour, title: "Approve for one hour", answer: .approval)
let approveAllDay = PermissionChoice
(id: AnswerIdentifier.approveAllDay, title: "Approve all day", answer: .approval)
let approveIndefinitely = PermissionChoice
(id: AnswerIdentifier.approveIndefinitely, title: "Approve indefinitely", answer: .approval)
let decline = PermissionChoice
(id: AnswerIdentifier.deny, title: "Decline", answer: .decline)
```

If your app requires a yes or no response, use the predefined [`PermissionChoice`](permissionchoice.md) options, [`approve`](permissionchoice/approve.md) and [`decline`](permissionchoice/decline.md):

```swift
public static let approve = PermissionChoice(id: approveChoiceIdentifier, title: "Approve", answer: .approval)
public static let decline = PermissionChoice(id: approveChoiceIdentifier, title: "Decline", answer: .decline)
```

Provide a default answer choice that reflects the experience expected when a child opts out of requesting experiences in iCloud Family settings managed by a parent or guardian, as shown below:

```swift
question.defaultChoice = approveIndefinitely
```

##### Send a Permission Question

To send a permission question, make an explicit request. When you call the `CommunicationLimits/ask(_:in:)-7lcls` method, the system validates the question, the sender, and the intended recipients. Depending on the specific scenario, the system displays the appropriate prompts, such as the new composed Message screen. You receive a [`PermissionResponse`](permissionresponse.md) as an `AsyncSequence` that you obtained earlier.

At any point during the send request flow, the child has the option to cancel the request, and decide not to send the question to their parent or guardian. In this scenario, the system doesn’t deliver a response to the calling app for that specific question.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/creating-a-communication-experience)*