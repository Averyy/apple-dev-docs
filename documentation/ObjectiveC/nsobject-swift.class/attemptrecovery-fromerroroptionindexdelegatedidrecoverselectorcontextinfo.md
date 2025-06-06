# attemptRecovery(fromError:optionIndex:delegate:didRecoverSelector:contextInfo:)

**Framework**: Objective-C Runtime  
**Kind**: method

Implemented to attempt a recovery from an error noted in a document-modal sheet.

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
func attemptRecovery(fromError error: any Error, optionIndex recoveryOptionIndex: Int, delegate: Any?, didRecoverSelector: Selector?, contextInfo: UnsafeMutableRawPointer?)
```

#### Discussion

Invoked when an error alert is presented to the user in a document-modal sheet, and the user has selected an error recovery option specified by `error`. After recovery is attempted, your implementation should send `delegate` the message specified in `didRecoverSelector`, passing the provided `contextInfo`.

The `didRecoverSelector` should have the following signature:

```objc
- (void)didPresentErrorWithRecovery:(BOOL)didRecover contextInfo:(void *)contextInfo;
```

where `didRecover` is [`YES`](yes.md) if the error recovery attempt was successful; otherwise it is [`NO`](no.md).

## Parameters

- `error`: An   object that describes the error, including error recovery options.
- `recoveryOptionIndex`: The index of the user selected recovery option in  ’s localized recovery array.
- `delegate`: An object that is the modal delegate.
- `didRecoverSelector`: A selector identifying the method implemented by the modal delegate.
- `contextInfo`: Arbitrary data associated with the attempt at error recovery, to be passed to   in  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/attemptrecovery(fromerror:optionindex:delegate:didrecoverselector:contextinfo:))*