# result(actionButtonIntent:dialog:)

**Framework**: Swift  
**Kind**: method

Indicates the Intent finished performing with an `AppIntent` to continue with

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
static func result<Intent>(actionButtonIntent: Intent, dialog: IntentDialog) -> Self where Self == IntentResultContainer<Never, Never, Never, IntentDialog>, Intent : AppIntent
```

## Parameters

- `actionButtonIntent`: The   used perform next
- `dialog`: A custom success dialog


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/never/result(actionbuttonintent:dialog:))*