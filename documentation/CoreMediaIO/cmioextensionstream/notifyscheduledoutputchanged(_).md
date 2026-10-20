# notifyScheduledOutputChanged(_:)

**Framework**: Core Media I/O  
**Kind**: method  
**Role**: Instance Method

Notifies clients when a particular buffer is output.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
func notifyScheduledOutputChanged(_ scheduledOutput: CMIOExtensionScheduledOutput)
```

```objc
- (void) notifyScheduledOutputChanged:(CMIOExtensionScheduledOutput *) scheduledOutput;
```

## Parameters

- `scheduledOutput`: The scheduled output.

## See Also

### Managing Scheduled Output
- [class CMIOExtensionScheduledOutput](../cmioextensionscheduledoutput.md)
  An object that represents scheduled output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionstream/notifyscheduledoutputchanged(_:))*