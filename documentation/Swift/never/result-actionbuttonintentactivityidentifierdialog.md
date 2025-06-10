# result(actionButtonIntent:activityIdentifier:dialog:)

**Framework**: Swift  
**Kind**: method

Indicates the Intent finished performing with an `AppIntent` to continue with

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- Mac Catalyst 17.2+
- macOS 14.2+
- tvOS 17.2+
- visionOS 1.0+
- watchOS 10.2+

## Declaration

```swift
static func result<Intent>(actionButtonIntent: Intent, activityIdentifier: String, dialog: IntentDialog) -> Self where Self == IntentResultContainer<Never, Never, Never, IntentDialog>, Intent : AppIntent
```

## Parameters

- `actionButtonIntent`: The   used perform next
- `dialog`: A custom success dialog


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/never/result(actionbuttonintent:activityidentifier:dialog:))*