# init(rotorType:itemSearchDelegate:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates a custom rotor with the specified rotor type and item search delegate.

**Availability**:
- macOS 10.13+

## Declaration

```swift
init(rotorType: NSAccessibilityCustomRotor.RotorType, itemSearchDelegate: any NSAccessibilityCustomRotorItemSearchDelegate)
```

```objc
- (instancetype) initWithRotorType:(NSAccessibilityCustomRotorType) rotorType itemSearchDelegate:(id<NSAccessibilityCustomRotorItemSearchDelegate>) itemSearchDelegate;
```

## See Also

### Creating a Rotor
- [init(label: String, itemSearchDelegate: any NSAccessibilityCustomRotorItemSearchDelegate)](./init%28label,itemsearchdelegate%29.md)
  Creates a custom rotor with the specified label and item search delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilitycustomrotor/init(rotortype:itemsearchdelegate:))*