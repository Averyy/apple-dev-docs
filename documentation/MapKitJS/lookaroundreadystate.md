# LookAroundReadyState

**Framework**: MapKit JS  
**Kind**: enum

Values that indicate the state of the Look Around object in the browser.

**Availability**:
- MapKit JS 5.79+

## Declaration

```swift
const LookAroundReadyState: Readonly<{
    readonly Loading: "loading";
    readonly Complete: "complete";
    readonly Error: "error";
    readonly Destroyed: "destroyed";
}>
```

## Topics

### Look Around object states
- [Complete](lookaroundreadystate/complete.md)
  A value that indicates the Look Around view has completed loading.
- [Destroyed](lookaroundreadystate/destroyed.md)
  A value that indicates the Look Around object is destroyed.
- [Error](lookaroundreadystate/error.md)
  A value that indicates the Look Around view encountered an error while loading.
- [Loading](lookaroundreadystate/loading.md)
  A value that indicates the Look Around view is loading.
### Type Aliases
- [type LookAroundReadyState](lookaroundreadystate/lookaroundreadystate.md)
  A type alias that represents the values of the look around ready state enumeration.

## See Also

- [element](abstractlookaround/element.md)
  A property that represents the Look Around view’s containing Document Object Model (DOM) element.
- [scene](abstractlookaround/scene.md)
  The Look Around scene the framework is displaying.
- [padding](abstractlookaround/padding.md)
  The padding options for the Look Around view.
- [readyState](abstractlookaround/readystate.md)
  A value that represents the loading state of the Look Around object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/lookaroundreadystate)*