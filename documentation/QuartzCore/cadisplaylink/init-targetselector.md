# init(target:selector:)

**Framework**: Core Animation  
**Kind**: init

Creates a display link for a target that calls its selector.

**Availability**:
- iOS 3.1+
- iPadOS 3.1+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(target: Any, selector sel: Selector)
```

#### Return Value

A new [`CADisplayLink`](cadisplaylink.md) object.

#### Discussion

The selector on the target must be a method with the following signature, where sender is the display link returned by this method.

The newly constructed display link retains the target.

## Parameters

- `target`: An object in your app that you want the system to notify each time it updates a display.
- `sel`: A selector instance that represents a method for  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/cadisplaylink/init(target:selector:))*