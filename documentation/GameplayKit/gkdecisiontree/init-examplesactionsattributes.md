# init(examples:actions:attributes:)

**Framework**: GameplayKit  
**Kind**: init

Creates an automatically learned decision tree using the specified attributes, example items, and actions.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
init(examples: [[any NSObjectProtocol]], actions: [any NSObjectProtocol], attributes: [any NSObjectProtocol])
```

#### Return Value

A new decision tree.

#### Discussion

When you use this initializer, the [`GKDecisionTree`](gkdecisiontree.md) class automatically infers a decision tree structure that chooses actions based on the attribute values in the examples array. That is, if you later use the [`findAction(forAnswers:)`](gkdecisiontree/findaction(foranswers:).md) method with a set of attribute values (or answers to questions) matching one of the entries in the `examples` array, the tree will choose the action at the corresponding index in the `actions` array. However, a decision tree is a predictive model, so the created tree is not limited to handling cases that exactly match the examples—if you call the [`findAction(forAnswers:)`](gkdecisiontree/findaction(foranswers:).md) with a set of answers not in the examples array, the tree predicts an action by generalizing from similar examples.

For example the following code creates a tree with data similar to that shown in [`Creating a Decision Tree`](gkdecisiontree#Creating-a-Decision-Tree.md):

**Swift**:

```swift
let attributes = [ "Type?", "HP?", "Special?" ]
let examples = [
    // Each sub-array has a value for each attribute:
    [ MyEnemyType.Electric.rawValue, 10, true ], // Note: enum value for the "Type?" attribute
    [ MyEnemyType.Electric.rawValue, 30, false ],
    [ MyEnemyType.Electric.rawValue, 40, true ],
    [ MyEnemyType.Fire.rawValue, 20, false ],
    [ MyEnemyType.Fire.rawValue, 30, false ],
    [ MyEnemyType.Water.rawValue, 50, true],
    [ MyEnemyType.Water.rawValue, 40, false ],
]
let actions = [ // One for each entry in the examples array
    "Psychic Strike",
    "Pound",
    "Barrier",
    "Pound",
    "Tackle",
    "Pound",
    "Tackle",
]
 
// Multiple type casts required to convert to collections of NSObjectProtocol in Swift
let decisionTree = GKDecisionTree(examples: examples as NSArray as! [[NSObjectProtocol]],
                                  actions: actions as NSArray as! [NSObjectProtocol],
                                  attributes: attributes as NSArray as! [NSObjectProtocol])
```

**Objective-C**:

```objc
NSArray *attributes = @[@"Type?", @"HP?", @"Special?"];
NSArray *examples = @[
    // Each sub-array has a value for each attribute:
    @[@(MyEnemyTypeElectric), @10, @YES],  // Note: enum value for the "Type?" attribute
    @[@(MyEnemyTypeElectric), @30, @NO],
    @[@(MyEnemyTypeElectric), @40, @YES],
    @[@(MyEnemyTypeFire), @20, @NO],
    @[@(MyEnemyTypeFire), @30, @NO],
    @[@(MyEnemyTypeWater), @50, @YES],
    @[@(MyEnemyTypeWater), @40, @NO],
];
NSArray *actions = @[ // One for each entry in the examples array
    @"Psychic Strike",
    @"Pound",
    @"Barrier",
    @"Pound",
    @"Tackle",
    @"Pound",
    @"Tackle",
];
 
GKDecisionTree *decisionTree = [[GKDecisionTree alloc] initWithExamples:examples actions:actions attributes:attributes];
```

When creating an automatically learned decision tree, be sure to provide enough examples to predict actions for all of the possible answer sets you expect to handle, and no contradictory examples.

For example, [`Figure 1`](gkdecisiontree#1965709.md) shows the tree inferred from the input in the above code example. This tree always chooses the “Psychic Strike” action when the opponent’s health is below 15, because the only example with that action fits that condition. If you want to choose that action based on answers to both the “HP?” and “Special?” attributes, you’d need to provide multiple examples where that action corresponds to different sets of attribute values.

## Parameters

- `examples`: An array of arrays. Each entry in the outer array is a list of example inputs, one for each attribute in the `attributes` array.
- `actions`: An array of actions. Each item in this array is the action, or final decision, corresponding to the example input at the same index in the `examples` array.
- `attributes`: An array of questions, or attributes to be tested by the decision tree. In the inner arrays of the `examples` array, each entry corresponds to the attribute at the same index in this array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkdecisiontree/init(examples:actions:attributes:))*