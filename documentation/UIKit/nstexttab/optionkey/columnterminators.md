# columnTerminators

**Framework**: UIKit  
**Kind**: property

The value is an `NSCharacterSet` object.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static let columnTerminators: NSTextTab.OptionKey
```

#### Discussion

The character set is used to determine the terminating character for a tab column. The tab and newline characters are implied even if they don’t exist in the character set. This attribute is optional.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstexttab/optionkey/columnterminators)*