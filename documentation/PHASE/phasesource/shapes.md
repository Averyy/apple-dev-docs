# shapes

**Framework**: PHASE  
**Kind**: property  
**Role**: Instance Property

An array of shapes that collectively define the audio-emitting surface area of a volumetric source.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var shapes: [PHASEShape] { get }
```

```objc
@property (nonatomic, copy, readonly) NSArray<PHASEShape *> * shapes;
```

#### Discussion

The framework sets the contents to the `shapes` argument of the [`init(engine:shapes:)`](./init%28engine,shapes%29.md) initializer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasesource/shapes)*