# attemptRecovery(optionIndex:resultHandler:)

**Framework**: Foundation  
**Kind**: method  
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

#### Discussion

This entry point is used for recovery of errors handled at a “document” granularity, that do not affect the entire application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/recoverableerror/attemptrecovery(optionindex:resulthandler:))*