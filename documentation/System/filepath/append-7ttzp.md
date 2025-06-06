# append(_:)

**Framework**: System  
**Kind**: method

Append the contents of `other`, ignoring any spurious leading separators.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
mutating func append(_ other: String)
```

#### Discussion

A leading separator is spurious if `self` is non-empty.

Example:

```swift
var path: FilePath = ""
path.append("/var/www/website") // "/var/www/website"
path.append("static/assets") // "/var/www/website/static/assets"
path.append("/main.css") // "/var/www/website/static/assets/main.css"
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filepath/append(_:)-7ttzp)*