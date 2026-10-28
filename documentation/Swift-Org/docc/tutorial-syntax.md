---
url: "https://docs.swift.org/latest/documentation/docc/tutorial-syntax"
framework: "Swift-Org/docc"
---

# Interactive Tutorials

**Framework**: Swift-Org/docc  
**Role**: API Collection

Teach developers your Swift APIs through step-by-step, interactive content.

## Overview

Use tutorials to deliver interactive documentation for your Swift frameworks and packages. Each tutorial augments your reference documentation by guiding readers through coding exercises that show how to build apps and projects that use your APIs in realistic ways.

![A screenshot of the landing page of an example tutorial called SlothCreator. The tutorial text reads ‘Meet SlothCreator. Create, catalog, and care for sloths using SlothCreator. Get started with SlothCreator by building the demo app Slothy.’ There’s an estimated time to complete the tutorial of 30 minutes, a ‘Get started’ button, and an illustration showing three iPhones with sloth artwork on them.](https://docs.swift.org/latest/images/org.swift.docc/6_tutorial_toc@2x.png)

You write tutorial content in Markdown, and use directives to define specific types of pages and elements, like introductions, sections, steps, and assessments. Then, you run the DocC compiler to render your tutorial in a rich, interactive learning format.

![A diagram that shows a blocked-out example of a Markdown document on that left, which contains directive syntax. On the right, a diagram shows a blocked-out example of compiled tutorial. Arrows between the two diagrams denote that the Markdown is translated into the tutorial documentation.](https://docs.swift.org/latest/images/org.swift.docc/interactive-tutorials@2x.png)

## Topics

### Essentials
- [Building an Interactive Tutorial](./building-an-interactive-tutorial.md)
  Construct a step-by-step guided learning experience for your Swift framework or package.
### Adding a Table of Contents
- [@Tutorials(...)](./tutorials.md)
  Displays a table of contents page for readers to navigate the pages of an interactive tutorial.
### Adding Tutorial Pages
- [@Tutorial(time: Int, projectFiles: ResourceReference)](./tutorial.md)
  Displays a tutorial page that teaches your Swift framework or package APIs through interactive coding exercises.
- [@Article(...)](./article.md)
  Displays a tutorial article page that teaches a conceptual topic about your Swift framework or package.
### Shared Syntax
- [Shared Directives](./tutorial-shared-directives.md)
  Directives supported by multiple directives in interactive tutorials.

## See Also

### Documentation Types
- [API Documentation](./api-reference-syntax.md)
  Teach your APIs through reference documentation you create from code comments and extension files, or create detailed articles and conceptual guides.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/docc/tutorial-syntax)*