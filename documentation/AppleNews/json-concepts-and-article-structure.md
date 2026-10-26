# JSON Concepts and Article Structure

**Framework**: Apple News  
**Role**: Article

Understand basic JSON concepts and become familiar with the structure of an Apple News Format article.

#### Overview

Before you start creating articles in Apple News Format, you want to make sure that you’re familiar with basic JSON concepts (including the use of objects, properties, and arrays) and that you understand how they relate to the JSON file you’re creating.

In this section you’ll learn about:

- How JSON uses name-value pairs to structure data
- The various types of values for properties
- The correct use of punctuation in a JSON file
- The structure of an Apple News Format article document file

You’ll also find information about the character sets Apple News Format supports.

##### Understand the Basic JSON Concepts of an Article Document File

You start an Apple News Format article by creating a JSON article document file with the name `article.json`. This file — along with images and other resource files — contains the information  the Apple News app needs to process and render your article.

###### An Article Is a JSON Object

At the most basic level, an `article.json` file contains a single JSON *object* — the [`ArticleDocument`](https://developer.apple.com/documentation/applenewsformat/articledocument) object. Like all JSON objects, the article document object begins and ends with curly brackets (`{}`) and is made up of *properties*.

###### An Object Has Properties Structured as Name-Value Pairs

Each property in a JSON object is a *name-value pair* (sometimes called a *key-value pair*). The name in a name-value pair is always enclosed in straight quotation marks, with a colon (`:`) separating the name from its value. For example, in the name-value pair for the following property, the name is `columns` and the value is `10:`

```json
"columns": 10
```

> 💡 **Tip**:  Add a space after the colon to make your code easier to read.

###### Values in Name-Value Pairs Can Take Many Forms

In JSON, the values in name-value pairs can be of various types, including:

- A string (enclosed in straight quotation marks)
- An integer or floating point number (as shown in the previous example)
- A Boolean (true or false) value
- An object (a list of properties enclosed in curly brackets)
- An array (a list of items enclosed in square brackets)

You’re probably familiar with string, integer, and Boolean as types of values, but the concept of using objects and arrays as values may be new to you. Compare the following examples.

###### Example 1

```json
"title": "Article Title"
```

The first example shows the name-value pair for a property called `"title"` whose value is a string (`"Article Title"`).

###### Example 2

```json
"layout": {   
  "columns": 20,
  "width": 1024,
  "margin": 60,
  "gutter": 20 
}
```

In the second example, the name-value pair is for a property called `"layout"` and the value is an object with four properties of its own. The object is enclosed in curly brackets and has commas separating the four properties. (Note that there’s no comma after the last property.)

###### Example 3

```json
"colorStops": [ 
  {
    "color": "honeydew",
   },            
   { 
    "color": "aliceblue",
   },
   { 
     "color": "seashell",
   },
]
```

The third example shows the name-value pair for a property called `"colorStops"` whose value is an array. The items in the array are enclosed in square brackets (`[]`) with commas separating them. In this example, the items in the array are objects — each is enclosed in curly brackets and each has a single property named `"color"`. Note that there’s no comma after the last item.

###### You Can Nest Properties

Because the value of a property can be an object or an array, properties are often nested inside other properties. For example, the following code shows a `heading1Layout` object with three properties (named `"columnStart"`, `"columnSpan"`, and `"margin"`). The value for the `"margin"` property is another object with two properties (`"top"` and `"bottom"`).

```json
"heading1Layout": {
	"columnStart": 0,
	"columnSpan": 7,
	"margin": {
	    "top": 24,
	    "bottom": 3
	}
} 
```

###### Some Properties Are Optional

Not all properties associated with an object are required. For example, the [`Layout`](https://developer.apple.com/documentation/applenewsformat/layout) component object has four properties (`columns`, `gutter`, `margin`, and `width`), but only two properties (`columns` and `width`) are required.

> **Note**:  If a property is required by Apple News Format, omitting the property generates an error in your code. Required properties are noted in the documentation for each object.

###### Punctuation Is Critical

Incorrect punctuation in your `article.json` file — even a misplaced comma or a curly quotation mark instead of a straight quote — generates an error when you try to preview your article. You must fix all errors before you can preview your article.

To avoid errors, make sure you follow these rules throughout your JSON code:

- You must enclose a name-value pair in straight quotation marks; put a colon (`:`) before the value.
- Enclose the list of properties in an object in curly brackets (`{}`). Use a comma to separate properties; don’t put a comma after the last property in the list.
- Enclose the list of items in an array in square brackets (`[]`). Use commas to separate items; don’t put a comma after the last item in the list.
- All values in name-value pairs have a data type. You must enclose values with a string data type in straight quotation marks. Don’t use quotation marks with integer or Boolean data types. When a value is an object, use curly brackets and separate the object properties with commas; use square brackets for values that are arrays.

###### The Structure of article.json

![Labeled screenshot of a sample article.json file that conforms to the punctuation rules.](https://developer.apple.com/tutorials/images/com.apple.applenews/media-3039444@2x.png)

###### Further Reading

To learn more about general JSON concepts, see [JSON.org](https://www.json.org).

##### Use HTML and Markdown in Your Code

In addition to the Apple News Format objects and properties, you can use a subset of HTML tags and Markdown syntax in your JSON document. For example, you can use HTML tags to create a list or use Markdown to specify a link.

Not all HTML tags and Markdown syntax are supported. For details, see [Using HTML with Apple News Format](./using-html-with-apple-news-format.md) and [Using Markdown with Apple News Format](./using-markdown-with-apple-news-format.md).

##### Use the Supported Character Sets

Apple News Format supports both ASCII and Unicode character sets. You can include characters directly or reference them by their Unicode value. For example, the following examples display the same thing: the words “Lorem ipsum” surrounded by curly quotation marks.

```json
"text": "“Lorem ipsum”"
"text": "\u201cLorem ipsum\u201d"
```

> **Note**:  Rendering support for Unicode values is dependent on the font you use. See [Applying Apple News Format Fonts](./applying-apple-news-format-fonts.md).

## See Also

### Essentials
- [Creating an Article: Main Steps](./creating-an-article-main-steps.md)
  Plan the design for your article and create it in Apple News Format.
- [object ArticleDocument](https://developer.apple.com/documentation/applenewsformat/articledocument)
  The root object of an Apple News article, that contains required properties, metadata, content, layout, and styles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenews/json-concepts-and-article-structure)*