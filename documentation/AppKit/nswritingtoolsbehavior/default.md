# NSWritingToolsBehavior.default

**Framework**: AppKit  
**Kind**: case  
**Role**: Case

An option to let the system determine the best way to enable Writing Tools for the view.

**Availability**:
- macOS 15.0+

## Declaration

```swift
case `default`
```

```c
NSWritingToolsBehaviorDefault
```

#### Discussion

The system chooses a complete, limited, or none experience based on the device-level support for the feature.

## See Also

### Getting the Writing Tools behaviors
- [NSWritingToolsBehavior.none](./none.md)
  An option to prevent Writing Tools from modifying the text in the view.
- [NSWritingToolsBehavior.complete](./complete.md)
  An option to provide the complete Writing Tools experience for the text view.
- [NSWritingToolsBehavior.limited](./limited.md)
  An option to provide a limited, overlay-panel experience for the text view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswritingtoolsbehavior/default)*