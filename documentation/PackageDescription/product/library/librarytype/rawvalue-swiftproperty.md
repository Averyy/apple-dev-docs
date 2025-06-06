# rawValue

**Framework**: PackageDescription  
**Kind**: property

The corresponding value of the raw type.

## Declaration

```swift
var rawValue: String { get }
```

#### Discussion

A new instance initialized with `rawValue` will be equivalent to this instance. For example:

```swift
enum PaperSize: String {
    case A4, A5, Letter, Legal
}

let selectedSize = PaperSize.Letter
print(selectedSize.rawValue)
// Prints "Letter"

print(selectedSize == PaperSize(rawValue: selectedSize.rawValue)!)
// Prints "true"
```

The corresponding value of the raw type.

A new instance initialized with `rawValue` will be equivalent to this instance.

## See Also

- [Product.Library.LibraryType.RawValue](product/library/librarytype/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/product/library/librarytype/rawvalue-swift.property)*