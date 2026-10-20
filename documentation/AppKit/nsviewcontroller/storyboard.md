# storyboard

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The storyboard from which the view controller was loaded.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var storyboard: NSStoryboard? { get }
```

```objc
@property (strong, readonly, nullable) NSStoryboard * storyboard;
```

#### Discussion

If the view controller was not loaded from a storyboard, the value of this property is `nil`.

## See Also

### Using a Storyboard
- [func dismiss(Any?)](./dismiss%28_%29-3n76y.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcontroller/storyboard)*