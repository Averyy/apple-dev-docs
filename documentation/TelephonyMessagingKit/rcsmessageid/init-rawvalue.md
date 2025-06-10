# init(rawValue:)

**Framework**: TelephonyMessagingKit  
**Kind**: init

Creates a new instance with the specified raw value.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
init(rawValue: String)
```

#### Discussion

If there is no value of the type that corresponds with the specified raw value, this initializer returns `nil`. For example:

```None
enum PaperSize: String {
    case A4, A5, Letter, Legal
}

print(PaperSize(rawValue: "Legal"))
// Prints "Optional(PaperSize.Legal)"

print(PaperSize(rawValue: "Tabloid"))
// Prints "nil"
```

## Parameters

- `rawValue`: The raw value to use for the new instance.

## See Also

- [let rawValue: String](rcsmessageid/rawvalue-swift.property.md)
  The corresponding value of the raw type.
- [RCSMessageID.RawValue](rcsmessageid/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsmessageid/init(rawvalue:))*