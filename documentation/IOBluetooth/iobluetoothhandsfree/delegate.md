# delegate

**Framework**: IOBluetooth  
**Kind**: property

Return the delegate

**Availability**:
- macOS 10.7+

## Declaration

```swift
unowned(unsafe) var delegate: (any IOBluetoothHandsFreeDelegate)! { get set }
```

#### Return Value

The delegate for the hands free object or nil if it doesn’t have a delegate.

#### Discussion

Returns the hands free object’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfree/delegate)*