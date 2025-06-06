# attemptRecovery(fromError:optionIndex:)

**Framework**: Objective-C Runtime  
**Kind**: method

Implemented to attempt a recovery from an error noted in an application-modal dialog.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func attemptRecovery(fromError error: any Error, optionIndex recoveryOptionIndex: Int) -> Bool
```

#### Return Value

[`YES`](yes.md) if the error recovery was completed successfully, [`NO`](no.md) otherwise.

#### Discussion

Invoked when an error alert is been presented to the user in an application-modal dialog, and the user has selected an error recovery option specified by `error`.

## Parameters

- `error`: An   object that describes the error, including error recovery options.
- `recoveryOptionIndex`: The index of the user selected recovery option in  ’s localized recovery array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/attemptrecovery(fromerror:optionindex:))*