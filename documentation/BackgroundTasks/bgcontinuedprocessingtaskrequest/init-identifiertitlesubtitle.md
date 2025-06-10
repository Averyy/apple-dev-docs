# init(identifier:title:subtitle:)

**Framework**: Background Tasks  
**Kind**: init

Creates an instance on behalf of the currently foregrounded app.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
init(identifier: String, title: String, subtitle: String)
```

#### Discussion

Apps and their extensions need to use this method to initialize any tasks due to the underlying association to the currently foregrounded app. Note that [`earliestBeginDate`](bgtaskrequest/earliestbegindate.md) is ignored by the scheduler in favor of `NSDate.now`.

The identifier must leverage a base wildcard notation, where the prefix of the identifier must at least contain the bundle ID of the submitting application, followed by optional semantic context, and finally ending with `.*`. An example: `<MainBundle>.<SemanticContext>.*` transforms to `com.foo.MyApplication.continuedProcessingTask.*`. Thus, a submitted identifier is of the form `com.foo.MyApplication.continuedProcessingTask.HD830D`.

> ⚠️ **Warning**:  Successful creation of this object does not guarantee successful submission to the scheduler.

## Parameters

- `identifier`: The task identifier.
- `title`: The localized title displayed to a person before the task begins running.
- `subtitle`: The localized subtitle displayed to a person before the task begins running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundtasks/bgcontinuedprocessingtaskrequest/init(identifier:title:subtitle:))*