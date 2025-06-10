# name

**Framework**: Swift  
**Kind**: property

Returns the human-readable name of the current task, if it was set during the tasks’ creation.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
static var name: String? { get }
```

#### Discussion

Tasks can be named during their creation, which can be helpful to identify unique tasks which may be created at same source locations, for example:

```swift
func process(items: [Int]) async {
  await withTaskGroup { group in
    for item in items {
      group.addTask(name: "process-\(item)") {
        await process(item)
      }
    }
  }
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/task/name)*