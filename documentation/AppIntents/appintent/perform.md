# perform()

**Framework**: App Intents  
**Kind**: method  
**Required**: Yes

Performs the intent’s action and returns a result, after resolving any parameters.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
func perform() async throws -> Self.PerformResult
```

## Mentions

- [Responding to the Action button on Apple Watch Ultra](actionbuttonarticle.md)
- [Creating your first app intent](creating-your-first-app-intent.md)
- [Getting started with the App Intents framework](getting-started-with-the-app-intents-framework.md)

#### Return Value

The result of the action. You can use the result to tell the system to perform additional actions. For example, include an `OpensAppIntent` type if you want the system to open your app and perform another action. You can also provide the system with dialog and snippet content along with the result.

#### Discussion

Implement this method in your custom type to perform the action in your app. Return a result or throw error to indicate the success or failure of the action.

Before calling this method, the system resolves your app intent’s parameters to known values. Use your implementation to perform the action using the provided information and deliver a result back to the system. At any point in your implementation, you can also use methods of the [`AppIntent`](appintent.md) protocol to request confirmation or ask someone to choose from a set of options you provide.

For information about how to implement this method, see [`Creating your first app intent`](creating-your-first-app-intent.md).

## See Also

- [var systemContext: IntentSystemContext](appintent/systemcontext.md)
  Contextual information that the system provides while it performs the app intent.
- [associatedtype PerformResult : IntentResult](appintent/performresult.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appintent/perform())*