# name

**Framework**: PackageDescription  
**Kind**: property

The name of the dependency.

**Availability**:
- SwiftPM ?+

## Declaration

```swift
var name: String? { get }
```

#### Discussion

If the `name` is `nil`, Swift Package Manager deduces the dependency’s name from its package identity or Git URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/package/dependency/name)*