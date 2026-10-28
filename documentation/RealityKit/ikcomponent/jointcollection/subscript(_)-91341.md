# subscript(_:)

**Framework**: RealityKit  
**Kind**: subscript  
**Role**: Instance Subscript

Accesses the element with the specified name.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
subscript(name: String) -> IKComponent.JointCollection.Element? { get set }
```

**Other overloads**:

```swift
subscript(id: IKComponent.JointCollection.Element.ID) -> IKComponent.JointCollection.Element? { get set }
```

## Overview

Has the same setter restrictions as `IKComponent/JointCollection/subscript(id:)`

## Parameters

- `name`: The name of the requested element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/ikcomponent/jointcollection/subscript(_:)-91341)*