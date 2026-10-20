# NSExpression

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

An expression for use in a comparison predicate.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class NSExpression
```

```objc
@interface NSExpression : NSObject
```

#### Overview

Comparison operations in an [`NSPredicate`](./nspredicate.md) derive from two expressions as instances of the [`NSExpression`](./nsexpression.md) class. You create expressions for constant values, key paths, and so on.

Generally, anywhere in the [`NSExpression`](./nsexpression.md) class hierarchy where there’s a composite API and subtypes that may only reasonably respond to a subset of that API, invoking a method that doesn’t make sense for that subtype throws an exception.

##### Aggregate Expressions

[`NSExpression.ExpressionType.aggregate`](./nsexpression/expressiontype-swift.enum/aggregate.md) allows you to create predicates containing expressions that evaluate to collections that contain further expressions. The collection may be an [`NSArray`](./nsarray.md), [`NSSet`](./nsset.md), or [`NSDictionary`](./nsdictionary.md) object.

Core Data doesn’t support aggregate expressions.

##### Subquery Expressions

The [`NSExpression.ExpressionType.subquery`](./nsexpression/expressiontype-swift.enum/subquery.md) creates a subexpression that returns a subset of a collection of objects. This allows you to create sophisticated queries across relationships, such as a search for multiple correlated values on the destination object of a relationship.

##### Set Expressions

The set expressions ([`NSExpression.ExpressionType.unionSet`](./nsexpression/expressiontype-swift.enum/unionset.md), [`NSExpression.ExpressionType.intersectSet`](./nsexpression/expressiontype-swift.enum/intersectset.md), and [`NSExpression.ExpressionType.minusSet`](./nsexpression/expressiontype-swift.enum/minusset.md)) combine results in a manner similar to the [`NSSet`](./nsset.md) methods.

Both sides of these expressions must evaluate to a collection; the left side must evaluate to an `NSSet` object, and the right side can be any other collection type.

```objc
(expression UNION expression)
(expression INTERSECT expression)
(expression MINUS expression)
```

Core Data doesn’t support set expressions.

##### Function Expressions

In macOS 10.4, [`NSExpression`](./nsexpression.md) only supports a predefined set of functions: `sum`, `count`, `min`, `max`, and `average`. You access these predefined functions in the predicate syntax using custom keywords (for example, `MAX(1, 5, 10)`).

In macOS 10.5 and later, function expressions also support arbitrary method invocations. To implement this extended functionality, use the syntax `FUNCTION(receiver, selectorName, arguments, ...),` as in the following example:

```objc
FUNCTION(@"/Developer/Tools/otest", @"lastPathComponent") => @"otest"
```

All methods must take one or more `id` arguments and return an `id` value, although you can use the `CAST` expression to convert datatypes with lossy string representations (for example, `CAST(####, "NSDate")`). macOS 10.5 extends the `CAST` expression to provide support for casting to classes for use in creating receivers for function expressions.

Although Core Data supports evaluation of the predefined functions, it doesn’t support the evaluation of custom predicate functions in the persistent stores (during a fetch).

## Topics

### Creating an Expression
- [init(expressionType: NSExpression.ExpressionType)](./nsexpression/init%28expressiontype%29.md)
  Creates the expression with the specified expression type.
- [init(format: String, argumentArray: [Any])](./nsexpression/init%28format,argumentarray%29.md)
  Creates the expression with the specified expression format and array of arguments.
- [init(format: String, arguments: CVaListPointer)](./nsexpression/init%28format,arguments%29.md)
  Creates the expression with the specified expression format and arguments list.
- [convenience init(format: String, any CVarArg...)](./nsexpression/init%28format,_%29.md)
  Creates the expression with the expression format and arguments list you specify.
- [init?(coder: NSCoder)](./nsexpression/init%28coder%29.md)
  Creates an expression by decoding from the coder you specify.
### Creating an Expression for a Value
- [init(forConstantValue: Any?)](./nsexpression/init%28forconstantvalue%29.md)
  Creates an expression that represents a specified constant value.
- [class func expressionForEvaluatedObject() -> NSExpression](./nsexpression/expressionforevaluatedobject%28%29.md)
  Creates an expression that represents the object you’re evaluating.
- [init(forKeyPath: String)](./nsexpression/init%28forkeypath%29-1aqf5.md)
  Creates an expression that invokes the value function with a specified key path.
- [init(forVariable: String)](./nsexpression/init%28forvariable%29.md)
  Creates an expression that extracts a value from the variable bindings dictionary for a specified key.
- [convenience init<Root, Value>(forKeyPath: KeyPath<Root, Value>)](./nsexpression/init%28forkeypath%29-98by.md)
  Creates an expression using a key path you specify.
- [class func expressionForAnyKey() -> NSExpression](./nsexpression/expressionforanykey%28%29.md)
  Creates an expression that represents any key for a Spotlight query.
### Creating a Collection Expression
- [init(forAggregate: [NSExpression])](./nsexpression/init%28foraggregate%29.md)
  Creates an aggregate expression for a specified collection.
- [init(forUnionSet: NSExpression, with: NSExpression)](./nsexpression/init%28forunionset,with%29.md)
  Creates an expression object that represents the union of a specified set and collection.
- [init(forIntersectSet: NSExpression, with: NSExpression)](./nsexpression/init%28forintersectset,with%29.md)
  Creates an expression object that represents the intersection of a specified set and collection.
- [init(forMinusSet: NSExpression, with: NSExpression)](./nsexpression/init%28forminusset,with%29.md)
  Creates an expression object that represents the subtraction of a specified collection from a specified set.
### Creating a Subquery
- [init(forSubquery: NSExpression, usingIteratorVariable: String, predicate: NSPredicate)](./nsexpression/init%28forsubquery,usingiteratorvariable,predicate%29.md)
  Creates an expression that filters a collection by storing elements in the collection in a specified variable and keeping the elements that the qualifier returns as true.
### Creating a Conditional Expression
- [init(forConditional: NSPredicate, trueExpression: NSExpression, falseExpression: NSExpression)](./nsexpression/init%28forconditional,trueexpression,falseexpression%29.md)
  Creates an expression that returns a result, depending on the value of predicate.
### Creating an Expression Using Blocks
- [init(block: (Any?, [NSExpression], NSMutableDictionary?) -> Any, arguments: [NSExpression]?)](./nsexpression/init%28block,arguments%29.md)
  Creates an expression object that uses the block for evaluating objects.
### Creating an Expression for a Function
- [init(forFunction: String, arguments: [Any])](./nsexpression/init%28forfunction,arguments%29.md)
  Creates an expression that invokes one of the predefined functions.
- [init(forFunction: NSExpression, selectorName: String, arguments: [Any]?)](./nsexpression/init%28forfunction,selectorname,arguments%29.md)
  Creates an expression that returns the result of invoking a selector with a specified name using specified arguments.
### Getting Information About an Expression
- [var arguments: [NSExpression]?](./nsexpression/arguments.md)
  The arguments for the expression.
- [var collection: Any](./nsexpression/collection.md)
  The collection of expressions in an aggregate expression, or the collection element of a subquery expression.
- [var constantValue: Any?](./nsexpression/constantvalue.md)
  The constant value of the expression.
- [var expressionType: NSExpression.ExpressionType](./nsexpression/expressiontype-swift.property.md)
  The expression type for the expression.
- [NSExpression.ExpressionType](./nsexpression/expressiontype-swift.enum.md)
  Defines the possible types of an expression.
- [var function: String](./nsexpression/function.md)
  The function for the expression.
- [var keyPath: String](./nsexpression/keypath.md)
  The key path for the expression.
- [var operand: NSExpression](./nsexpression/operand.md)
  The operand for the expression.
- [var predicate: NSPredicate](./nsexpression/predicate.md)
  The predicate of a subquery expression.
- [var left: NSExpression](./nsexpression/left.md)
  The left expression of an aggregate expression.
- [var right: NSExpression](./nsexpression/right.md)
  The right expression of an aggregate expression.
- [var variable: String](./nsexpression/variable.md)
  The variable for the expression.
### Evaluating an Expression
- [func expressionValue(with: Any?, context: NSMutableDictionary?) -> Any?](./nsexpression/expressionvalue%28with,context%29.md)
  Evaluates an expression using a specified object and context.
- [func allowEvaluation()](./nsexpression/allowevaluation%28%29.md)
  Forces a securely decoded expression to allow evaluation.
- [var `false`: NSExpression](./nsexpression/false.md)
  An expression to evalutate if a conditional expression’s predicate evaluates to false.
- [var `true`: NSExpression](./nsexpression/true.md)
  An expression to evalutate if a conditional expression’s predicate evaluates to true.
### Accessing the Expression Block
- [var expressionBlock: (Any?, [NSExpression], NSMutableDictionary?) -> Any](./nsexpression/expressionblock.md)
  The block that executes to evaluate the expression.
### Initializers
- [convenience init?<Input, Output>(Expression<Input, Output>)](./nsexpression/init%28_%29.md)
- [init(forBlock: (Any?, [NSExpression], NSMutableDictionary?) -> Any, arguments: [NSExpression]?)](./nsexpression/init%28forblock,arguments%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](./nscoding.md)
- [NSCopying](./nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](./nssecurecoding.md)

## See Also

### Filltering
- [struct Predicate](./predicate.md)
  A logical condition used to test a set of input values for searching or filtering.
- [struct PredicateError](./predicateerror.md)
  An error thrown while evaluating a predicate.
- [struct PredicateCodableConfiguration](./predicatecodableconfiguration.md)
  A specification of the expected types and key paths found in an archived predicate.
- [protocol PredicateCodableKeyPathProviding](./predicatecodablekeypathproviding.md)
  A type that provides the expected key paths found in an archived predicate.
- [protocol PredicateExpression](./predicateexpression.md)
  A component expression that makes up part of a predicate.
- [protocol StandardPredicateExpression](./standardpredicateexpression.md)
  A component expression that makes up part of a predicate, and that’s supported by the standard predicate type.
- [enum PredicateExpressions](./predicateexpressions.md)
  The expressions that make up a predicate.
- [struct PredicateBindings](./predicatebindings.md)
  A mapping from a predicates’s input variables to their values.
- [class NSPredicate](./nspredicate.md)
  A definition of logical conditions for constraining a search for a fetch or for in-memory filtering.
- [class NSComparisonPredicate](./nscomparisonpredicate.md)
  A specialized predicate for comparing expressions.
- [class NSCompoundPredicate](./nscompoundpredicate.md)
  A specialized predicate that evaluates logical combinations of other predicates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsexpression)*