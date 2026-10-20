# scriptingBegins(with:)

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Returns `true` if, in a scripting comparison, the compared object matches the beginning of `object`.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
func scriptingBegins(with object: Any) -> Bool
```

```objc
- (BOOL) scriptingBeginsWith:(id) object;
```

## See Also

### Performing comparisons
- [func scriptingContains(Any) -> Bool](./scriptingcontains%28_%29.md)
  Returns `true` if, in a scripting comparison, the compared object contains `object`.
- [func scriptingEnds(with: Any) -> Bool](./scriptingends%28with%29.md)
  Returns `true` if, in a scripting comparison, the compared object matches the end of `object`.
- [func scriptingIsEqual(to: Any) -> Bool](./scriptingisequal%28to%29.md)
  Returns `true` if, in a scripting comparison, the compared object is equal to `object`.
- [func scriptingIsGreaterThan(Any) -> Bool](./scriptingisgreaterthan%28_%29.md)
  Returns `true` if, in a scripting comparison, the compared object is greater than `object`.
- [func scriptingIsGreaterThanOrEqual(to: Any) -> Bool](./scriptingisgreaterthanorequal%28to%29.md)
  Returns `true` if, in a scripting comparison, the compared object is greater than or equal to `object`.
- [func scriptingIsLessThan(Any) -> Bool](./scriptingislessthan%28_%29.md)
  Returns `true` if, in a scripting comparison, the compared object is less than `object`.
- [func scriptingIsLessThanOrEqual(to: Any) -> Bool](./scriptingislessthanorequal%28to%29.md)
  Returns `true` if, in a scripting comparison, the compared object is less than or equal to `object`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/scriptingbegins(with:))*