# startingItemNumber

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Sets the starting item number for the text list.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var startingItemNumber: Int { get set }
```

```objc
@property NSInteger startingItemNumber;
```

#### Discussion

The default value is `1`. This value will be used only for ordered lists, and ignored in other cases.

## Parameters

- `itemNum`: The item number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextlist/startingitemnumber)*