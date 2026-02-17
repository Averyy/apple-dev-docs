# name

**Framework**: PackageDescription  
**Kind**: property

The trait’s canonical name.

**Availability**:
- SwiftPM 6.1+

## Declaration

```swift
var name: String
```

#### Discussion

Use the trait’s name to enable the trait or when referring to it from other modifiers in the manifest. The trait’s name also defines the conditional block that the compiler supports when the trait is active.

The following rules are enforced on trait names:

- The first character must be a [`Unicode XID start character`](https://developer.apple.comhttps://unicode.org/reports/tr31/#Figure_Code_Point_Categories_for_Identifier_Parsing) (most letters), a digit, or `_`.
- Subsequent characters must be a [`Unicode XID start character`](https://developer.apple.comhttps://unicode.org/reports/tr31/#Figure_Code_Point_Categories_for_Identifier_Parsing) (a digit, `_`, or most letters), `-`, or `+`.
- The names `default` and `defaults` (in any letter casing combination) aren’t allowed as trait names to avoid confusion with default traits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/trait/name)*