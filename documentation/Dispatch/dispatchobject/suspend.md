# suspend()

**Framework**: Dispatch  
**Kind**: method

Suspends the invocation of block objects on a dispatch object.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func suspend()
```

#### Discussion

By suspending a dispatch object, your application can temporarily prevent the execution of any blocks associated with that object. The suspension occurs after completion of any blocks running at the time of the call. Calling this function increments the suspension count of the object, and calling [`resume()`](dispatchobject/resume().md) decrements it. While the count is greater than zero, the object remains suspended, so you must balance each [`suspend()`](dispatchobject/suspend().md) call with a matching [`resume()`](dispatchobject/resume().md) call.

Any blocks submitted to a dispatch queue or events observed by a dispatch source are delivered once the object is resumed.

> ❗ **Important**:  It is a programmer error to release an object that is currently suspended, because suspension implies that there is still work to be done. Therefore, always balance calls to this method with a corresponding call to [`resume()`](dispatchobject/resume().md) before disposing of the object. The behavior when releasing the last reference to a dispatch object while it is in a suspended state is undefined.

 It is a programmer error to release an object that is currently suspended, because suspension implies that there is still work to be done. Therefore, always balance calls to this method with a corresponding call to [`resume()`](dispatchobject/resume().md) before disposing of the object. The behavior when releasing the last reference to a dispatch object while it is in a suspended state is undefined.

## See Also

- [func activate()](dispatchobject/activate.md)
  Activates the dispatch object.
- [func resume()](dispatchobject/resume.md)
  Resumes the invocation of block objects on a dispatch object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchobject/suspend())*