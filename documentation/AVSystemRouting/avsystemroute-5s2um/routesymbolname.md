# routeSymbolName

**Framework**: AVSystemRouting  
**Kind**: property

The SF Symbol name representing the remote device or route.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
final var routeSymbolName: String { get }
```

## Mentions

- [Routing and streaming media to remote devices](routing-and-streaming-media-to-remote-devices.md)

#### Discussion

This property returns a system symbol name as a `String` that identifies the type of device (such as a TV, speaker, or other compatible endpoint). Use this value with `Image(systemName:)` to create an icon for display in your app’s user interface.

```swift
let routeIcon = Image(systemName: route.routeSymbolName)
```

The symbol helps people visually identify where their media will be played.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avsystemrouting/avsystemroute-5s2um/routesymbolname)*