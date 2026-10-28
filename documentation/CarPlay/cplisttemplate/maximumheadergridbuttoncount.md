# maximumHeaderGridButtonCount

**Framework**: CarPlay  
**Kind**: property  
**Role**: Type Property

The maximum number of grid buttons that may appear in a @c CPListTemplate.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
class var maximumHeaderGridButtonCount: Int { get }
```

```objc
@property (class, nonatomic, readonly) NSUInteger maximumHeaderGridButtonCount;
```

## Discussion

> **Note**: Your list template will display the first @c maximumHeaderGridButtonCount buttons. Any sections beyond that limit will be trimmed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplisttemplate/maximumheadergridbuttoncount)*