# init(attributedName:itemSearch:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a rotor with the specified name and search block.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
init(attributedName: NSAttributedString, itemSearch itemSearchBlock: @escaping UIAccessibilityCustomRotor.Search)
```

```objc
- (instancetype) initWithAttributedName:(NSAttributedString *) attributedName itemSearchBlock:(UIAccessibilityCustomRotorSearch) itemSearchBlock;
```

## Return Value

An initialized rotor object.

## Parameters

- `attributedName`: The name of the rotor.
- `itemSearchBlock`: The block that provides the next or previous rotor.

## See Also

### Creating a rotor object
- [init(name: String, itemSearch: UIAccessibilityCustomRotor.Search)](./init%28name,itemsearch%29.md)
  Creates a rotor with the specified name and search block.
- [init(systemType: UIAccessibilityCustomRotor.SystemRotorType, itemSearch: UIAccessibilityCustomRotor.Search)](./init%28systemtype,itemsearch%29.md)
  Creates a rotor for the specified type of item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilitycustomrotor/init(attributedname:itemsearch:))*