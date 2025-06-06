# init(path:)

**Framework**: Foundation  
**Kind**: init

Initializes an `NSDistributedLock` object to use as the lock the file-system entry specified by a given path.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
init?(path: String)
```

#### Return Value

An `NSDistributedLock` object initialized to use as the locking object the file-system entry specified by `path`.

#### Discussion

For applications to use the lock, `path` must be accessible to—and writable by—all hosts on which the applications might be running.

## Parameters

- `path`: All of   up to the last component itself must exist. You can use   to create (and set permissions) for any nonexistent intermediate directories.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdistributedlock/init(path:))*