# subscript(_:)

**Framework**: SwiftUI  
**Kind**: subscript  
**Role**: Instance Subscript

Reads an observable object of the specified type from the environment.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
subscript<T>(objectType: T.Type) -> T? where T : AnyObject, T : Observable { get set }
```

**Other overloads**:

```swift
subscript<K>(key: K.Type) -> K.Value where K : EnvironmentKey { get set }
```

```swift
subscript<K>(key: K.Type) -> K.Value where K : UITraitBridgedEnvironmentKey { get set }
```

## Return Value

The environment object of the specified type, or `nil` if no object of that type has been set in this environment.

## Overview

> ❗ **Important**: This subscript only supports reading objects that conform to the `Observable` protocol.

Use this subscript to read the environment object of a specific type from an instance of [`EnvironmentValues`](../environmentvalues.md), such as when accessing the [`environment`](../graphicscontext/environment.md) property of a graphics context:

```swift
@Observable final class Profile { ... }

Canvas { context, size in
    let currentProfile = context.environment[Profile.self]
    ...
}
```

## Parameters

- `objectType`: The type of the `Observable` object to read from the environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/subscript(_:)-43hzl)*