# donate(result:)

**Framework**: App Intents  
**Kind**: method

Donates the intent and optional result to the transcript.

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
@discardableResult
func donate(result: some IntentResult) -> IntentDonationIdentifier
```

#### Discussion

This synchronous method is available to applications that haven’t adopted Swift async concurrency. The system ignores any exceptions encountered when donating this intent.

## See Also

- [func donate() async throws -> IntentDonationIdentifier](appintent/donate-1e60c.md)
  Donates the intent to the transcript.
- [func donate() -> IntentDonationIdentifier](appintent/donate-jp6k.md)
  Donates the intent to the transcript.
- [func donate(result: some IntentResult) async throws -> IntentDonationIdentifier](appintent/donate(result:)-36cia.md)
  Donates the intent and optional result to the transcript.
- [func callAsFunction(donate: Bool) async throws -> Self.PerformResult.Value](appintent/callasfunction(donate:)-3qvbt.md)
- [func callAsFunction(donate: Bool) async throws](appintent/callasfunction(donate:)-7v1om.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appintent/donate(result:)-9b25i)*