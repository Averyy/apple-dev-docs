# init(coder:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates a Touch Bar object from a coder object provided by a storyboard or NIB file.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.12.2+

## Declaration

```swift
init?(coder: NSCoder)
```

```objc
- (instancetype) initWithCoder:(NSCoder *) coder;
```

#### Return Value

A fully initialized Touch Bar object, or `nil` if the coder doesn’t define a Touch Bar object.

## See Also

### Creating a bar
- [init()](./init%28%29.md)
  Creates a Touch Bar object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstouchbar/init(coder:))*