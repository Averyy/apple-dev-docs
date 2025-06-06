# rawValue

**Framework**: ManagedSettings  
**Kind**: property

The corresponding value of the raw type.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/safarisettings/cookiepolicy-swift.enum/rawvalue-swift.property)*