# init(forSubquery:usingIteratorVariable:predicate:)

**Framework**: Foundation  
**Kind**: init

Creates an expression that filters a collection by storing elements in the collection in a specified variable and keeping the elements that the qualifier returns as true.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(forSubquery expression: NSExpression, usingIteratorVariable variable: String, predicate: NSPredicate)
```

#### Return Value

An expression that filters a collection by storing elements in the collection in the variable variable and keeping the elements for which qualifier returns true

#### Discussion

This method creates a sub-expression, evaluation of which returns a subset of a collection of objects. It allows you to create sophisticated queries across relationships, such as a search for multiple correlated values on the destination object of a relationship.

For example, suppose you have an Apartment entity that has a to-many relationship to a Resident entity, and that you want to create a query for all apartments inhabited by a resident whose first name is “Jane” and whose last name is “Doe”. Using only API available for OS X v 10.4, you could try the predicate:

```objc
resident.firstname == "Jane" && resident.lastname == "Doe"
```

but this will always return false since `resident.firstname` and `resident.lastname` both return collections. You could also try:

```objc
resident.firstname CONTAINS "Jane" && resident.lastname CONTAINS "Doe"
```

but this is also flawed—it returns true if there are two residents, one of whom is John Doe and one of whom is Jane Smith. The only way to find the desired apartments is to do two passes: one through residents to find “Jane Doe”, and one through apartments to find the ones where our Jane Does reside.

Subquery expressions provide a way to encapsulate this type of qualification into a single query.

The string format for a subquery expression is:

```objc
SUBQUERY(collection_expression, variable_expression, predicate);
```

where `expression` is a predicate expression that evaluates to a collection, `variableExpression` is an expression which will be used to contain each individual element of `collection`, and `predicate` is the predicate used to determine whether the element belongs in the result collection.

Using subqueries, the apartment query could be reformulated as

```objc
(SUBQUERY(residents, $x, $x.firstname == "Jane" && $x.lastname == "Doe").@count != 0)
```

or

```objc
(SUBQUERY(residents, $x, $x.firstname == "Jane" && $x.lastname == "Doe")[size] != 0)
```

## Parameters

- `expression`: A predicate expression that evaluates to a collection.
- `variable`: Used as a local variable, and will shadow any instances of variable in the bindings dictionary. The variable is removed or the old value replaced once evaluation completes.
- `predicate`: The predicate used to determine whether the element belongs in the result collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsexpression/init(forsubquery:usingiteratorvariable:predicate:))*