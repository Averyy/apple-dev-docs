# init(label:itemSearchDelegate:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates a custom rotor with the specified label and item search delegate.

**Availability**:
- macOS 10.13+

## Declaration

```swift
init(label: String, itemSearchDelegate: any NSAccessibilityCustomRotorItemSearchDelegate)
```

```objc
- (instancetype) initWithLabel:(NSString *) label itemSearchDelegate:(id<NSAccessibilityCustomRotorItemSearchDelegate>) itemSearchDelegate;
```

## See Also

### Creating a Rotor
- [init(rotorType: NSAccessibilityCustomRotor.RotorType, itemSearchDelegate: any NSAccessibilityCustomRotorItemSearchDelegate)](./init%28rotortype,itemsearchdelegate%29.md)
  Creates a custom rotor with the specified rotor type and item search delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilitycustomrotor/init(label:itemsearchdelegate:))*