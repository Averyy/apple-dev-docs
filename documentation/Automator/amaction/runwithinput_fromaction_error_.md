# runWithInput:fromAction:error:

**Framework**: Automator  
**Kind**: method  
**Role**: Instance Method

Requests the action to perform its task using the specified input from the specified action.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+ - Deprecated in 10.4

> **Deprecated**: Use [`run(withInput:)`](./run%28withinput%29.md) instead.

## Declaration

```objc
- (id) runWithInput:(id) input fromAction:(AMAction *) anAction error:(NSDictionary<NSString *,id> **) errorInfo;
```

#### Return Value

An object containing one or more objects of a data type compatible with a type specified in the receiving action’s `AMProvides` property. If the action doesn’t modify the data passed in `input`, it should return it unchanged.

#### Discussion

The input and output objects for actions are usually instances of [`NSArray`](../../Foundation/nsarray.md). If the action encounters problems, it should return by indirection an error dictionary that describes the error.

This method is intended to be overridden. AppleScript actions, however, usually will not need to override this method because the same functionality is provided by an AppleScript script.

## Parameters

- `input`: The input for the receiving action. By default, actions can only accept and provide the following types. However, by overriding this method, you can change the types your action can use:

  - Objective-C actions: Accepts and provides types must inherit from `com.apple.cocoa.string`, `com.apple.cocoa.path`, `com.apple.cocoa.url`, or `com.apple.cocoa.data`.
  - Shell script actions: Accepts and provides types must inherit from `com.apple.cocoa.string` or `com.apple.cocoa.data`.
  - AppleScript actions: Accepts and provides types must inherit from `com.apple.applescript.object`.
- `anAction`: The action from which the `input` object was obtained.
- `errorInfo`: If an error occurs, the action returns an error dictionary in this parameter. The keys and values for this dictionary are:

  - `OSAScriptErrorNumber` (a string constant) — The value for this key is an instance of [`NSNumber`](../../Foundation/nsnumber.md) whose integer value indicates an error code. See the header file `MacErrors.h` in the Carbon Core framework for a list of valid error codes, particularly the section on OSA errors.
  - `OSAScriptErrorMessage` (a string constant) —The value for this key is an instance of [`NSString`](../../Foundation/nsstring.md) describing the error.

## See Also

### Deprecated
- [- didFinishRunningWithError:](./didfinishrunningwitherror_.md)
  Sent by the action to itself when it has finished running asynchronously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amaction/runwithinput:fromaction:error:)*