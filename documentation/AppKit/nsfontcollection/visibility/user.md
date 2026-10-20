# user

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

The font collection is visible to all processes and is stored persistently.

**Availability**:
- macOS

## Declaration

```swift
static var user: NSFontCollection.Visibility { get }
```

```c
NSFontCollectionVisibilityUser
```

## See Also

### Visibility Options
- [static var process: NSFontCollection.Visibility](./process.md)
  The font collection is visible within this process and is not persistent.
- [static var computer: NSFontCollection.Visibility](./computer.md)
  The font collection is visible to all users and is stored persistently.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontcollection/visibility/user)*