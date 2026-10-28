# attemptRecovery(optionIndex:resultHandler:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Attempt to recover from this error when the user selected the option at the given index. This routine must call handler and indicate whether recovery was successful (or not).

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func attemptRecovery(optionIndex recoveryOptionIndex: Int, resultHandler handler: @escaping (Bool) -> Void)
```

## Discussion

This entry point is used for recovery of errors handled at a “document” granularity, that do not affect the entire application.

## Default Implementations

### RecoverableError Implementations
- [func attemptRecovery(optionIndex: Int, resultHandler: (Bool) -> Void)](./attemptrecovery%28optionindex,resulthandler%29-1zbgz.md)
  Default implementation that uses the application-model recovery mechanism ([`attemptRecovery(optionIndex:)`](./attemptrecovery%28optionindex%29.md)) to implement document-modal recovery.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/recoverableerror/attemptrecovery(optionindex:resulthandler:))*