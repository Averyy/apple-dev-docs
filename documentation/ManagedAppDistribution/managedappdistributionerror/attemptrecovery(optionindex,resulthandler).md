# attemptRecovery(optionIndex:resultHandler:)

**Framework**: ManagedAppDistribution  
**Kind**: method  
**Role**: Instance Method

Attempt to recover from this error when someone selects the option at the given index.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 2.4+

## Declaration

```swift
func attemptRecovery(optionIndex recoveryOptionIndex: Int, resultHandler handler: @escaping (Bool) -> Void)
```

## See Also

### Recovering from errors
- [func attemptRecovery(optionIndex: Int) -> Bool](./attemptrecovery%28optionindex%29.md)
  Attempt to recover from this error when someone selects the option at the given index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedappdistribution/managedappdistributionerror/attemptrecovery(optionindex:resulthandler:))*