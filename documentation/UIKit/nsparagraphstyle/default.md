# default

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

The default paragraph style.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
@NSCopying
class var `default`: NSParagraphStyle { get }
```

```objc
@property (class, nonatomic, copy, readonly) NSParagraphStyle * defaultParagraphStyle;
```

#### Discussion

The default paragraph style has the following default values:

| Subattribute | Default |
| --- | --- |
| Alignment | `NSNaturalTextAlignment` |
| Tab stops | 12 left-aligned tabs, spaced by `28.0` points |
| Line break mode | `NSLineBreakByWordWrapping` |
| All others | `0.0` |

See individual method descriptions for explanations of each subattribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsparagraphstyle/default)*