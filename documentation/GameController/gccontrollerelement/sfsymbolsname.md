# sfSymbolsName

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property

A system symbol for the element or the remapped element.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var sfSymbolsName: String? { get set }
```

```objc
@property (nonatomic, strong, nullable) NSString * sfSymbolsName;
```

## Discussion

If the user remaps this element, this property is the remapped system symbol.

## See Also

### Displaying a symbol
- [var unmappedSfSymbolsName: String?](./unmappedsfsymbolsname.md)
  The element’s system symbol, not the remapped symbol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontrollerelement/sfsymbolsname)*