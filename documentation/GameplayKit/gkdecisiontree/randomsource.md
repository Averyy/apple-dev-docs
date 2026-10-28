# randomSource

**Framework**: GameplayKit  
**Kind**: property  
**Role**: Instance Property

The randomizer to be used when evaluating parts of the tree that branch randomly.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var randomSource: GKRandomSource { get set }
```

```objc
@property (nonatomic, copy) GKRandomSource * randomSource;
```

## Discussion

Some of the branches in a decision tree may not depend on an external input; instead, when evaluating the tree with the [`findAction(forAnswers:)`](./findaction%28foranswers%29.md) method, the tree automatically chooses an answer at random. (In a manually created decision tree, you can create random branches with the [`createBranch(weight:attribute:)`](../gkdecisionnode/createbranch%28weight,attribute%29.md) method.) The tree uses this random source when randomly choosing answers.

## See Also

### Evaluating a Tree to Make Decisions
- [func findAction(forAnswers: [AnyHashable : any NSObjectProtocol]) -> (any NSObjectProtocol)?](./findaction%28foranswers%29.md)
  Searches the decision tree, following the branches corresponding to each of the specified answers, and returns the resulting action object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkdecisiontree/randomsource)*