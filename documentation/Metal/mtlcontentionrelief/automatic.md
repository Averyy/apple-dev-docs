# MTLContentionRelief.automatic

**Framework**: Metal  
**Kind**: case  
**Role**: Case

Adds contention relief when the kernel lacks other forms.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
case automatic
```

```c
MTLContentionReliefAutomatic
```

## Discussion

The implementation inserts contention relief when the kernel doesn’t include other mechanisms, such as `metal::atomic_wait_*` functions or explicit calls to `metal::yield_simdgroup`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcontentionrelief/automatic)*