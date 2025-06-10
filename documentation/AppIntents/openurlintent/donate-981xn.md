# donate()

**Framework**: App Intents  
**Kind**: method

Donates the intent to the transcript.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
@discardableResult
func donate() -> IntentDonationIdentifier
```

#### Discussion

This synchronous method is available to applications that haven’t adopted Swift async concurrency. The system ignores any exceptions encountered when donating this intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/openurlintent/donate()-981xn)*