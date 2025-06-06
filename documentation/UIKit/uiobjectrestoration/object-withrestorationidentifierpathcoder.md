# object(withRestorationIdentifierPath:coder:)

**Framework**: Uikit  
**Kind**: method  
**Required**: Yes

Requests the object that corresponds to the specified identifier information.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
static func object(withRestorationIdentifierPath identifierComponents: [String], coder: NSCoder) -> (any UIStateRestoring)?
```

#### Return Value

The object to use or `nil` if you do not want to restore this object now.

#### Discussion

Your implementation of this method should create (or find) the corresponding object and return it. If your restoration class determines that the object shouldn’t be restored, it may return `nil` from this method.

You use the strings in the `identifierComponents` parameter to identify the object being requested. The object may be at the end of a restoration hierarchy containing your app’s view controllers and other objects. The strings in the `identifierComponents` array identify the path through this hierarchy to the desired object.

It isn’t always necessary to create a new object in your implementation of this method. You can also return an existing object that was created by another means. For example, if the object had already been created by your app delegate at initialization time, you’d return that object rather than create a new one.

Your implementation of this method may use any data in the provided `coder` to assist in the restoration process. However, you don’t need to restore the entire state of the object at this point. During a later pass, objects that define a [`decodeRestorableState(with:)`](uiviewcontroller/decoderestorablestate(with:).md) method are given a chance to restore their state from the same coder object.

> **Note**:  If you return an object whose class doesn’t match the class of the originally preserved object, or whose class isn’t a direct subclass of the original, the restoration system doesn’t call the [`decodeRestorableState(with:)`](uiviewcontroller/decoderestorablestate(with:).md) method of the object.

## Parameters

- `identifierComponents`: An array of   objects corresponding to the restoration identifiers of the desired object and all of its ancestors in the restoration hierarchy. The last value in the array is the restoration identifier of the desired object. Earlier entries represent the restoration identifiers of its ancestors.
- `coder`: The keyed archiver containing the app’s saved state information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiobjectrestoration/object(withrestorationidentifierpath:coder:))*