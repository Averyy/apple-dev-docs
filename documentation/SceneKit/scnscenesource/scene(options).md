# scene(options:)

**Framework**: SceneKit  
**Kind**: method  
**Role**: Instance Method

Instantiates a scene from the scene source with the specified options.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
func scene(options: [SCNSceneSource.LoadingOption : Any]? = nil) throws -> SCNScene
```

```objc
- (SCNScene *) sceneWithOptions:(NSDictionary<NSString *,id> *) options error:(NSError **) error;
```

#### Return Value

An [`SCNScene`](../scnscene.md) object containing the entire scene graph from the scene source, or `nil` if loading was not successful.

#### Discussion

Calling this method is equivalent to calling [`scene(options:statusHandler:)`](./scene%28options,statushandler%29.md) with a block that checks its `error` parameter to see whether the status is [`SCNSceneSourceStatus.error`](../scnscenesourcestatus/error.md). To load a scene without creating a scene source object, use the [`SCNScene`](../scnscene.md) method [`init(url:options:)`](../scnscene/init%28url,options%29-7ugvv.md).

A scene source can contain objects that are not part of its scene graph. To obtain these objects, you must load them individually with the the [`entryWithIdentifier:withClass:`](./entrywithidentifier_withclass_.md) or [`entries(passingTest:)`](./entries%28passingtest%29.md) method. For example, a scene file containing a game character could include several animations for the character geometry (such as running, jumping, and standing idle). Because you typically do not apply multiple animations at once, the scene file contains these animations without their being attached to the character geometry.

> **Handling Errors in Swift**:  In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `options`: A dictionary containing options that affect scene loading. See `Scene Loading Options` for available keys and values. Pass `nil` to use default options.

## See Also

### Loading a Complete Scene
- [func scene(options: [SCNSceneSource.LoadingOption : Any]?, statusHandler: SCNSceneSourceStatusHandler?) -> SCNScene?](./scene%28options,statushandler%29.md)
  Loads the entire scene graph from the scene source and calls the specified block to provide progress information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscenesource/scene(options:))*