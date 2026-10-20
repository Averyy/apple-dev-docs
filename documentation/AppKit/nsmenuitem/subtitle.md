# subtitle

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- macOS 14.4+

## Declaration

```swift
var subtitle: String? { get set }
```

```objc
@property (copy, nullable) NSString * subtitle;
```

#### Discussion

Used to specify a standard subtitle for the menu item.

The subtitle is displayed below the standard title.

> **Note**: On macOS 14, a menu item with an attributed title does not show the subtitle. The subtitle is shown on macOS 15 and later.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenuitem/subtitle)*